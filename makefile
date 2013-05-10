all:
	@python condiciones.py
	@python runge.py
	@python graficador.py

clean:
	@rm -f *.txt
	@rm -f *.png
