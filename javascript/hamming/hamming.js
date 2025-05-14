export const compute = (strandA, strandB) => {
  if (strandA.length !== strandB.length) {
    throw new Error('strands must be of equal length');
  }
  let diff = 0;
  for (let i = 0; i < strandA.length; i++) {
    if (strandA[i] !== strandB[i]) {
      diff++;
    }
  }
  return diff;
};
