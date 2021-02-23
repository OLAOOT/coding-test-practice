function solution(bridge_length, weight, truck_weights) {
  let answer = 0;
  
  const trucks = truck_weights.map((v) => ({
      w: v,
      loc: 1
  }))
  
  const bridge = []
  
  const curWeight = () => bridge.length === 0 ? 0 : bridge.reduce((cur, v) => cur + v.w, 0)
  
  while (true) {
      if (trucks.length === 0 && bridge.length === 0) 
          break;
      else if (trucks.length !== 0 && bridge.length === 0) {
          bridge.push(trucks.shift())
          answer++
      }
      else if (trucks.length === 0) {
          const time = bridge_length - bridge[bridge.length - 1].loc + 1
          bridge.length = 0
          answer += time
      }
      else {
          bridge.forEach(v => {
              v.loc++
          })
          answer++
          if (bridge[0].loc > bridge_length)
              bridge.shift()
          if (curWeight() + trucks[0].w <= weight)
              bridge.push(trucks.shift())
      }
  }
  
  return answer;
}