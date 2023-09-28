library(seewave)
library(tuneR)
sound1 = readMP3("sax_jazz.mp3")
sound2 = readMP3("brownian_noise.mp3")
sound3 = readMP3("arigato.mp3")
# comando necesario para que funcione en mac
tuneR::setWavPlayer('/usr/bin/afplay')

# vemos la metadata
sound1
sound2
sound3

# oscilograma de los sonidos
oscillo(sound1, title="Sonido 1");axis(side=2, las=2)
oscillo(sound2, title="Sonido 2");axis(side=2, las=2)
oscillo(sound3, title="Sonido 3");axis(side=2, las=2)
# zoom
oscillo(sound1, from=3, to=3.01, title="🔎 Sonido 1");axis(side=2, las=2)
oscillo(sound2, from=0.1, to=0.2, title="🔎 Sonido 2");axis(side=2, las=2)
oscillo(sound3, from=0.2, to=0.3, title="🔎 Sonido 3");axis(side=2, las=2)

# normalize
sound1B = normalize(sound1,unit='16',level=0.1)
oscillo(sound1B, title="Sonido 1 Normalized");axis(side=2, las=2)

# sound test
play(sound1)
play(sound1B)

# spec
spec(sound1, main="Sonido 1");axis(side=2, las=2)
spec(sound2, main="Sonido 2");axis(side=2, las=2)
spec(sound3, main="Sonido 3");axis(side=2, las=2)

# spectro
spectro(sound1);title(main="Sound 1")
spectro(sound2);title(main="Sound 2")
spectro(sound3);title(main="Sound 3")

# pasa bajo
sound1PB=ffilter(sound1,to=5000,output="Wave")
sound1PB=normalize(sound1PB,unit='16')
spectro(sound1PB);title(main="Sonido 1 Paso Bajo")

# paso alto
sound1PA=ffilter(sound1,from=5000,output="Wave")
sound1PA=normalize(sound1PA,unit='16')
spectro(sound1PA);title(main="Sonido 1 Paso Alto")