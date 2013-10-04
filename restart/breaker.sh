for i in *.tex
do
  fold -sw 80 $i > $i
done