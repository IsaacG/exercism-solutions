// Package diffiehellman provides Diffie-Hellman-Merkle key exchange
package diffiehellman

import (
	"math/big"
	"math/rand"
	"time"
)

// PrivateKey generates a private key, randomly selected from [2, p)
// The key must be greater than 1. Rand(n) gives [0, n) so we need to
// add two to the result to always be greater than 1.
func PrivateKey(p *big.Int) *big.Int {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	max := big.NewInt(0).Sub(p, big.NewInt(2))
	val := big.NewInt(0).Rand(r, max)
	return val.Add(val, big.NewInt(2))
}

// PublicKey generates a public key, A = g**a mod p
func PublicKey(private, p *big.Int, g int64) *big.Int {
	return big.NewInt(0).Exp(big.NewInt(g), private, p)
}

// NewPair returns a paired PublicKey and PrivateKey.
func NewPair(p *big.Int, g int64) (private, public *big.Int) {
	private = PrivateKey(p)
	public = PublicKey(private, p, g)
	return
}

// SecretKey generates the secrey key, s = B**a mod p
func SecretKey(private1, public2, p *big.Int) *big.Int {
	return big.NewInt(0).Exp(public2, private1, p)
}
