// Package account provides a bank account.
package account

import "sync"

// Account provides a bank account.
// If any Account method is called on an closed account, it must not modify
// the account and must return ok = false.
type Account struct {
	sync.RWMutex
	balance int64
	open    bool
}

// Open returns a new Account.
// If Open is given a negative initial deposit, it must return nil.
func Open(initialDeposit int64) *Account {
	if initialDeposit < 0 {
		return nil
	}
	return &Account{
		balance: initialDeposit,
		open:    true,
	}
}

// Close will close an account.
func (a *Account) Close() (payout int64, ok bool) {
	a.Lock()
	defer a.Unlock()
	if !a.open {
		return 0, false
	}
	a.open = false
	return a.balance, true
}

// Balance returns the account balance.
func (a *Account) Balance() (balance int64, ok bool) {
	a.RLock()
	defer a.RUnlock()
	if !a.open {
		return 0, false
	}
	return a.balance, true
}

// Deposit alters the account balance.
// It is thread safe.
// Deposit must handle a negative amount as a withdrawal. Withdrawals must
// not succeed if they result in a negative balance.
func (a *Account) Deposit(amount int64) (newBalance int64, ok bool) {
	a.Lock()
	defer a.Unlock()
	if !a.open || a.balance+amount < 0 {
		return 0, false
	}
	a.balance += amount
	return a.balance, true
}
