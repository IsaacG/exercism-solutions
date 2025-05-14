export const getCardPosition = (stack, card) => stack.indexOf(card);
export const doesStackIncludeCard = (stack, card) => stack.includes(card);
export const isEachCardEven = (stack) => stack.every((n) => !(n % 2));
export const doesStackIncludeOddCard = (stack) => !isEachCardEven(stack);
export const getFirstOddCard = (stack) => stack.find((n) => n % 2);
export const getFirstEvenCardPosition = (stack) => stack.findIndex((n) => !(n % 2));
