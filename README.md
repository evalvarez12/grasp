# Grasp
[![Build Status](https://travis-ci.org/evalvarez12/grasp.svg?branch=master)](https://travis-ci.org/evalvarez12/grasp)


A text processor that identifies uncommon/foreign words, marks them and provides a definition.

Source
==========
Grasp is powered by [es.wikipedia.org](https://es.wikipedia.org/wiki/Wikipedia:Portada) as the training corpus and [es.wiktionary.org](https://es.wiktionary.org/wiki/Wikcionario:Portada) as the definitions sources.

Example
===========
 
Input :
 
 
	En informática, un núcleo o kernel (de la raíz germánica Kern, núcleo, hueso) es un software
	que constituye una parte fundamental del sistema operativo.
	
Output :

tado es el siguiente:

	En informática, un núcleo o [[kernel]] (de la raíz [[germánica]] Kern, núcleo, hueso) es un software
	que constituye una parte fundamental del sistema operativo.

	--- kernel ---
	sustantivo masculino Español
	1 Informática: Núcleo de un sistema operativo, es decir, bloque de código 
	con la parte central del funcionamiento y arranque del sistema.
	sinónimo núcleo.
	sustantivo Inglés
	1: núcleo de un fruto seco o similar, parte generalmente comestible del mismo.
	2: Núcleo, centro.
	3: semilla, grano, particularmente de trigo o maíz.
	4: hueso de un fruto, carozo, cuesco, güito.

	--- germánica ---
	1: forma adjetivo lengua: Español germánico género femenino .
	
Coming soon 
============
An API that facilitates integration into websites.



