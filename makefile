all:
	@python condiciones.py
	@python runge.py

clean:
	@rm -f *.txt
	@rm -f *.png
