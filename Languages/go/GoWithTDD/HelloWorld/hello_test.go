package main

import "testing"

func TestHello(t *testing.T) {
	got := Hello("World")
	want := "Hello, World"

	if got != want {
		t.Errorf("got %q, want %q", got, want)
	}
}

func TestHelloWithArg(t *testing.T) {
	got := Hello("Chris")
	want := "Hello, Chris"

	if got != want {
		t.Errorf("got %q, want %q", got, want)
	}
}
