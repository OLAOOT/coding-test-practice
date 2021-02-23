function solution(jobs) {
  let answer = 0
  let jobs_length = jobs.length
  const heap = [0]
  
  const insertHeap = (job) => {
      let i = heap.length
      while (i !== 1 && heap[parseInt(i / 2)][1] > job[1]) {
          heap[i] = heap[parseInt(i / 2)]
          i = parseInt(i / 2)
      }
      heap[i] = job
  }
  
  const deleteHeap = () => {
      if (heap.length === 1)  return 0
      if (heap.length === 2) {
          return heap.pop()
      }
      const root = heap[1]
      heap[1] = heap[heap.length - 1]
      const temp = heap[1]
      heap.length = heap.length - 1
      let i = 1
      
      while (heap[i * 2]) {
          const child = heap[i * 2 + 1] && heap[i * 2][1] > heap[i * 2 + 1][1] ? i * 2 + 1 : i * 2
          if (temp[1] > heap[child][1]) {
              heap[i] = heap[child]
              i = child
          }
          else    break
      }
      heap[i] = temp
      
      return root
  }
  
  jobs.sort((a, b) => a[0] - b[0])
  let time = jobs[0][0]
  
  while (jobs.length !== 0 || heap.length !== 1) {
      while (jobs.length !== 0 && jobs[0][0] <= time) {
          insertHeap(jobs[0])
          jobs.shift()
      }
      if (heap.length === 1) {
          time = jobs[0][0]
          continue
      }
      
      time += heap[1][1]
      answer += time - heap[1][0]
      deleteHeap()
  }
  return parseInt(answer / jobs_length)
}