var selectedCards = (
                from userCard in _dbSetUserCards
                join card in _dbSetCards on userCard.CardId equals card.Id
                select new
                {
                    CardNumber = card.Number,
                    CardId = card.Id,
                    userCard.AutoReplenishBalance,
                    userCard.AutoReplenishSum,
                    userCard.NotificationSum,
                    userCard.BankCardId,
                    userCard.UserId,
                    card.BalanceDate,
                    userCard.AutoReplenishEnabled,
                    card.TypeId,
                    card.Balance,
                    card.TripCount
                }).ToList();
            
            var selectedCardsWithSelectedCardTypes = (
                from selectedCard in selectedCards
                join cardType in _dbSetCardTypes on selectedCard.TypeId equals cardType.Id
                select new
                {
                    selectedCard.CardNumber,
                    CardTypeCode = cardType.Code,
                    selectedCard.CardId,
                    selectedCard.AutoReplenishBalance,
                    selectedCard.AutoReplenishSum,
                    selectedCard.NotificationSum,
                    selectedCard.BankCardId,
                    selectedCard.UserId,
                    selectedCard.BalanceDate,
                    selectedCard.AutoReplenishEnabled,
                    cardType.BalanceType,
                    CardReplenishType = cardType.ReplenishType,
                    // TODO: тут нужно что-то добавить или изменить
                    Balance = cardType.BalanceType == 0? selectedCard.Balance: selectedCard.TripCount
                }).ToList();
            
            // Select 3 таблиц. Cards, CardTypes, BankCards
            var userCardToUpdate = (
                from selectedCardsWithSelectedCardType in selectedCardsWithSelectedCardTypes.DefaultIfEmpty()
                join bankCard in _dbSetBankCards on selectedCardsWithSelectedCardType.BankCardId equals bankCard.Id into allColumns
                from useCardsToUpdate in allColumns.DefaultIfEmpty(new BankCard() )
                select new
                {
                    selectedCardsWithSelectedCardType.CardNumber,
                    selectedCardsWithSelectedCardType.CardTypeCode,
                    selectedCardsWithSelectedCardType.CardId,
                    selectedCardsWithSelectedCardType.AutoReplenishBalance,
                    selectedCardsWithSelectedCardType.AutoReplenishSum,
                    selectedCardsWithSelectedCardType.NotificationSum,
                    selectedCardsWithSelectedCardType.BankCardId,
                    selectedCardsWithSelectedCardType.UserId,
                    selectedCardsWithSelectedCardType.BalanceDate,
                    selectedCardsWithSelectedCardType.AutoReplenishEnabled,
                    selectedCardsWithSelectedCardType.BalanceType,
                    BankCardStatus = useCardsToUpdate.Status,
                    selectedCardsWithSelectedCardType.CardReplenishType,
                    selectedCardsWithSelectedCardType.Balance
                }).ToList();
            
            var lastTrips = _dbSetTrips.GroupBy(trip => new { trip.CardNumber, trip.CardTypeCode })
                .Select(e => new
                {
                    e.Key.CardNumber,
                    e.Key.CardTypeCode,
                    BalanceDate = e.Max(d=>d.BalanceDate)
                }).ToList();
            // в таблице trips проводится поиск записей, которые имеют свежую дату и при этом минимальный баланс. Записи в этой таблице каждые 3 месяца стираются
            var lastBalances = (
                from trip in _dbSetTrips
                join lastTrip in lastTrips on new { trip.CardNumber, trip.CardTypeCode, trip.BalanceDate } equals new
                {
                    lastTrip.CardNumber, lastTrip.CardTypeCode, lastTrip.BalanceDate
                } into allColumns
                group trip by new { trip.CardNumber, trip.CardTypeCode, trip.BalanceDate }
                into groupTrip
                select new
                {
                    groupTrip.Key.CardNumber,
                    groupTrip.Key.CardTypeCode,
                    Balance = groupTrip.Min(e => e.Balance),
                    groupTrip.Key.BalanceDate
                }).ToList();
            
            // Конечный список данных, которые нужны для воркера, чтобы обновить данные в таблицах
            var newBalancesList = (
                from lastBalance in lastBalances
                join userCard in userCardToUpdate on new { lastBalance.CardNumber, lastBalance.CardTypeCode } equals new
                {
                    userCard.CardNumber, userCard.CardTypeCode
                }
                join activeReplenish in _dbSetAutoReplenishes on userCard.CardId equals activeReplenish.CardId
                where userCard.BalanceDate < lastBalance.BalanceDate
                select userCard!=null && lastBalance!=null ?new CardBalanceQuery
                {
                    CardId = userCard.CardId,
                    NewBalanceDate = lastBalance.BalanceDate,
                    UserId = userCard.UserId,
                    AutoReplenishBalance = userCard.AutoReplenishBalance,
                    AutoReplenishSum = userCard.AutoReplenishSum,
                    NotificationSum = userCard.NotificationSum,
                    BankCardId = userCard.BankCardId,
                    AutoReplenishEnabled = userCard.AutoReplenishEnabled,
                    NewBalance = userCard.BalanceType == 0? lastBalance.Balance: 0,
                    NewTripCount = userCard.BalanceType == 0?(int)lastBalance.Balance: -1,
                    NewBalanceForCompare = lastBalance.Balance,
                    OldBalanceForCompare = userCard.Balance
                }: new CardBalanceQuery()
            );;
            return newBalancesList.ToList();