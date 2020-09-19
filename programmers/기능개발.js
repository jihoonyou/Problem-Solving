/*
기능개발
https://programmers.co.kr/learn/courses/30/lessons/42586?language=javascript
*/
function solution(progresses, speeds) {
    let answer = [];
    let queue = [];
    let day = 0;
    for (let i = 0; i < progresses.length; i++) {
        let required = 100 - progresses[i];
        queue.push(Math.ceil(required/speeds[i]));
    }
    
    while (queue.length) {
        console.log(queue)    
        if (day < queue[0]) {
            day += (queue[0] - day);
        }
        else {
            let count = 0;
            while (queue && day >= queue[0]) {
                queue.shift()
                count += 1;
            }
            answer.push(count);
        }
    }
    console.log(answer)
    return answer;
}
