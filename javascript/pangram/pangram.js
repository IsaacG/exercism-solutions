export const isPangram = (data) => {
  const seen = new Set(data.toLowerCase().match(/[a-z]/g));
  return seen.size === 26;
};
