def round_pain(real_efforts, pining):
	assert(len(real_efforts)==len(pining))
	pain = 0
	zipped_efforts = zip(real_efforts, pining)
	for effort in zipped_efforts:
		for e in effort:
			pain += e**2
	return pain

real_effort = [0.3, 0.05, 0.18]
pining 		= [0.2, 0.25, 0.02]
print round_pain(real_effort, pining)
