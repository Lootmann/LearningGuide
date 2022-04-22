package iteration

const repCount = 5

func Repeat(character string) string {
	repeated := ""
	for i := 0; i < repCount; i++ {
		repeated += character
	}
	return repeated
}
