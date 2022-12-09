class Company {
    constructor() {
        this.departments = {};
    }

    addEmployee(name, salary, position, department) {
        if (name === '' || name === undefined || name === null || salary < 0 || salary === undefined || salary === null || salary === '' || position === '' || position === undefined || position === null || department === '' || department === undefined || department === null) {
            throw Error('Invalid input!');
        }

        if (!(this.departments.hasOwnProperty(department))) {
            this.departments[department] = [{name, salary, position}];
        } else {
            this.departments[department].push({name, salary, position});
        }
        return `New employee is hired. Name: ${name}. Position: ${position}`;
    }

    bestDepartment() {
        let bestDepartment;
        let bestAvgSalary = 0;
        let bestDepartmentName;

        for (const departmentName in this.departments) {
            let currentTotalSalary = 0;
            for (const obj of this.departments[departmentName]) currentTotalSalary += obj.salary;
            const currentAvgSalary = currentTotalSalary / this.departments[departmentName].length;
            if (currentAvgSalary > bestAvgSalary) {
                bestAvgSalary = currentAvgSalary;
                bestDepartment = this.departments[departmentName];
                bestDepartmentName = departmentName;
            }

        }
        bestDepartment.sort((a, b) => {
            if (a.salary > b.salary) return -1;
            if (a.salary < b.salary) return 1;
            if (a.name > b.name) return 1;
            if (a.name < b.name) return -1;
        });

        let result = `Best Department is: ${bestDepartmentName}\nAverage salary: ${bestAvgSalary.toFixed(2)}\n`;
        for (const {name, salary, position} of bestDepartment) {
            result += `${name} ${salary} ${position}\n`;
        }
        return result.trim();
    }
}
