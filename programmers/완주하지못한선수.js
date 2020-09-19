function solution(participant, completion) {
    let answer = '';
    let completion_map = {}

    for (let i = 0; i < completion.length; i++) {
        let key =  completion[i]
        if (key in completion_map) {
            completion_map[key] += 1
        }
        else {
            completion_map[key] = 1
        }
    }

    for (let i = 0; i < participant.length; i++) {
        let key = participant[i]
        if ( !(key  in completion_map)) {
            console.log(key)
            return key
        }
        else {
            completion_map[key] -= 1

            if (completion_map[key] == 0) {
                delete completion_map[key]
            }
        }
    }
    
    return answer;
}

solution(["leo", "kiki", 'eden'],['eden', 'kiki'])