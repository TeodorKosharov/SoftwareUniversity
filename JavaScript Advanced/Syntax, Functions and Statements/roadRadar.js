function solve(speed, area) {
    function info(maxSpeed, currentSpeed) {
        if (currentSpeed <= maxSpeed) console.log(`Driving ${currentSpeed} km/h in a ${maxSpeed} zone`);
        else {
            let difference = speed - maxSpeed;
            let status = '';
            if (difference <= 20) status = 'speeding';
            else if (difference > 20 && difference <= 40) status = 'excessive speeding';
            else status = 'reckless driving';
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${maxSpeed} - ${status}`);
        }
    }

    if (area == 'motorway') info(130, speed);
    else if (area == 'interstate') info(90, speed);
    else if (area == 'city') info(50, speed);
    else info(20, speed);

}
