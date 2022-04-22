package contains

func Contains(str, found string) bool {
	for _, character := range str {
		if string(character) == found {
			return true
		}
	}

	return false
}
