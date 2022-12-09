function solve(arr) {
    let lectures = Number(arr.shift());
    let bonus = Number(arr.shift());
    let points = 0;
    let maxPoints = 0;
    let studentAttendances = 0;

    for (let attendance of arr) {
        points = Number(attendance) / lectures * (5 + bonus);
        if (points > maxPoints) {
            maxPoints = points;
            studentAttendances = attendance;
        }
    }

    console.log(`Max Bonus: ${Math.ceil(maxPoints)}.`);
    console.log(`The student has attended ${studentAttendances} lectures.`);
}
