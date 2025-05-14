const words = getCommonWords()
const targetWord = getTargetWord()

class Wordle {
  constructor (words, target) {
    this.words = words;                // Word list to use as a guess
    this.target = target;              // The target word
    this.contains = new Set(target);   // Letters contained in the targer
                                       // Known correct letters
    this.correct = [null, null, null, null, null];
    this.present = {};                 // Known present letters and where they are _not_ located.
    this.absent = new Set();           // Known absent letters
    this.guessIdx = 0;                 // Which word we are up to when guessing
  }

  isOver () {
    return !this.correct.includes(null)
  }
  
  // Evaluate a guess, updating our known state and returning the row results.
  evaluateGuess(guess) {
    const result = ["absent", "absent", "absent", "absent", "absent"]
    const unaccounted = {}
    // Check for correct letters and tally up unguessed/potential present letters
    for (let i = 0; i < 5; i++) {
      if (guess[i] == this.target[i]) {
        result[i] = "correct"
        this.correct[i] = guess[i]
      } else {
        unaccounted[this.target[i]] = (unaccounted[this.target[i]] || 0) + 1
      }
    }
    // Mark letters present.
    for (let i = 0; i < 5; i++) {
      if (result[i] == "absent" && unaccounted[guess[i]]) {
        result[i] = "present";
        unaccounted[guess[i]]--;
        this.present[guess[i]] || (this.present[guess[i]] = new Set())
        this.present[guess[i]].add(i)
      }
    }
    // Add absent letters.
    (new Set(guess)).difference(this.contains).forEach(x => this.absent.add(x))
    return result
  }

  // Check if a guess ought to be skipped based on known state.
  badGuess(guess) {
    // Check for letters we know are present but are missing from the guess.
    if (Object.keys(this.present).some(x => !guess.includes(x))) {
      return true
    }
    return [...guess].some((letter, i) => {
      // Check for known correct letters
      if (this.correct[i] && letter != this.correct[i]) {
        return true
      }
      // Check for known absent letters
      if (this.absent.has(letter)) {
        return true
      }
      // Check for letters we know and present but not in this location.
      if (this.present[letter] && this.present[letter].has(i)) {
        return true
      }
    })
    return false
  }

  nextGuess() {
    let guess;
    do {
      guess = this.words[this.guessIdx++];
    } while(this.badGuess(guess));
    return guess;
  }

  play() {
    let guessIdx = 0;
    
    for (let numGuess = 0; numGuess < 6 && !this.isOver(); numGuess++) {
      const guess = this.nextGuess();
      addWord(numGuess, guess, this.evaluateGuess(guess));
    }
  }
}

export function playGame() {
  new Wordle(words, targetWord).play()
}
