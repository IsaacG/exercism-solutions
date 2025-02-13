package airportrobot

import "fmt"

type Greeter interface {
	LanguageName() string
	Greet(name string) string
}

type Italian struct{}

func (i Italian) LanguageName() string     { return "Italian" }
func (i Italian) Greet(name string) string { return fmt.Sprintf("Ciao %s!", name) }

type Portuguese struct{}

func (i Portuguese) LanguageName() string     { return "Portuguese" }
func (i Portuguese) Greet(name string) string { return fmt.Sprintf("Olá %s!", name) }

func SayHello(name string, greeter Greeter) string {
	return fmt.Sprintf("I can speak %s: %s", greeter.LanguageName(), greeter.Greet(name))
}
