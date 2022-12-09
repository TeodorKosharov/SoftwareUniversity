function solve(arr) {
    let employeesHours = arr.slice(0, 3).map(x => Number(x));
    let totalEmpHours = 0;
    for (let el of employeesHours) totalEmpHours += el;
    let studentsHours = Number(arr.pop());
    let currentHour = 1;

    while (studentsHours > 0) {
        if (currentHour % 4 == 0) {
            currentHour++;
            continue;
        }
        studentsHours -= totalEmpHours;
        currentHour++;
    }
    console.log(`Time needed: ${currentHour - 1}h.`);
}
