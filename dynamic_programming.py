# Elaf Abdullah Saleh Alhaddad - 31063977

# Assignment 2 - Task 1
def best_schedule(weekly_income, competitions):
    """
    :param weekly_income: is a list of non-negative integers, where weekly_income[i] is the amount of money you will
    earn working as personal trainer in week i.
    :param competitions: a list of tuples, each representing a sporting competition.
        tuple[0] - is the week that the athlete will need to begin preparing for this competition
        tuple[1] - is the week that the athlete will need to spend recovering
        tuple[2] - is the profit made
    :return: the maximum profit that can be made by the athlete by doing the combination of these activities when suitable
    :time complexity: O(N log N) - N is the total number of elements in weekly_income and competitions
    :Space complexity: O(N) - N is the total number of elements in weekly_income and competitions
    """
    if len(weekly_income) == 0:  # If there is no weekly income
        return 0
    # Change the weekly income to be in the same format as competitions
    for i in range(len(weekly_income)):  # O(w) - w is the number of elements in the list weekly_income
        weekly_income[i] = (i, i, weekly_income[i])

    # Combine the two together in one list O(N)
    activities = []
    for i in range(len(weekly_income)):
        activities.append(weekly_income[i])
    for j in range(len(competitions)):
        activities.append(competitions[j])

    # sort the activities in order based on the ending time
    activities = sorted(activities, key=lambda x: x[1])  # O(N log(N))

    # Memoization
    memo = [0] * (activities[len(activities) - 1][1] + 2)  # O(N)
    memo[0] = 0  # No profit made
    memo[1] = activities[0][2]  # Profit taken for week 0
    for i in range(1, len(activities)):  # O(N)
        if activities[i][0] > activities[i - 1][1]:
            memo[activities[i][1] + 1] = memo[activities[i][1]] + activities[i][2]
        else:
            pos = memo[activities[i][0]] + activities[i][2]
            if pos > memo[activities[i][1] + 1]:
                memo[activities[i][1] + 1] = pos

    return memo[len(memo) - 1]


# Assignment 2 - Task 2
def best_itinerary(profit, quarantine_time, home):
    """
    :param profit: a list of lists. profit[i][j] is the profit that can be made by the salesperson by working in city j
    on day i
    :param quarantine_time: a list of non-negative integers. quarantine_time[i] is the number of days city i requires
    visitors to quarantine before they can work there
    :param home: an integer which represents the city that the salesperson starts in without needing to quarantine on the
    first day
    :return: maximum profit that can be earned by the salesperson
    :space complexity: O(nd) - n is the number of cities and d is the number of days
    :time complexity: O(nd) - n is the number of cities and d is the number of days
    """
    # Memoization O(nd)
    memo = [None] * (len(profit) + 1)
    for i in range(len(memo)):
        memo[i] = [0] * len(quarantine_time)

    # Last day used as base case
    memo[len(memo) - 2] = profit[len(profit) - 1]

    # Loop to calculate the maximum profit that can be gained in each city
    i = len(profit) - 2
    while i >= 0: # O(d)
        j = len(quarantine_time) - 1
        while j >= 0: # O(n)
            # possible sum 1 - if they stay in the same city
            pos = memo[i + 1][j] + profit[i][j]

            # possible sum 2 - the neighbouring city on the left
            if not (j == 0):
                if i < len(profit) - 1 - quarantine_time[j - 1]:
                    pos1 = memo[i + 1 + quarantine_time[j - 1]][j - 1]
                    if pos1 > pos:
                        pos = pos1

            # Possible sum 3 - the neighbouring city on the right
            if not (j == (len(quarantine_time) - 1)):
                if i < len(profit) - 1 - quarantine_time[j + 1]:
                    pos2 = memo[i + 1 + quarantine_time[j + 1]][j + 1]
                    if pos2 > pos:
                        pos = pos2

            # Possible sum 4 - cities on the left
            if not (j == 0):
                if i < len(profit) - 1:
                    pos4 = memo[i + 1][j - 1]
                    not_move = memo[i + 2][j - 1] + profit[i + 1][j - 1]
                    if not (pos4 == not_move):
                        if pos4 > pos:
                            pos = pos4

            # Possible sum 5 - cities on the right
            if not (j == (len(quarantine_time) - 1)):
                if i < len(profit) - 1:
                    pos5 = memo[i + 1][j + 1]
                    not_move = memo[i + 2][j + 1] + profit[i + 1][j + 1]
                    if not (pos5 == not_move):
                        if pos5 > pos:
                            pos = pos5

            memo[i][j] = pos
            j -= 1
        i -= 1
    return memo[0][home]
