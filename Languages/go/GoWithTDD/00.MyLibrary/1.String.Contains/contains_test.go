package contains

import "testing"

func TestContains(t *testing.T) {
	str := "abcdefg"
	found := "d"

	expected := true
	want := Contains(str, found)

	if expected != want {
		t.Errorf("expected, want = %t, %t", expected, want)
	}
}

func TestContainsFalse(t *testing.T) {
	str := "abcefg"
	found := "d"

	expected := false
	want := Contains(str, found)

	if expected != want {
		t.Errorf("expected, want = %t, %t", expected, want)
	}
}

func BenchmarkContains(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Contains("abcdefghijklmnopqrstuvwxyz", "z")
	}
}
