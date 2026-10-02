def validate_age(age):
	return age >= 18


def validate_email(email):
	return "@" in email and "." in email
