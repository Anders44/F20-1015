
FN=Lect-23
DIR=../..
PP=`pwd`

PY=  \
	add1.py \
	inv.py \
	mat2.png \
	mat3.png \
	mat8.png \
	matmul1.py \
	matmul2.py \
	mul0.png \
	mul1.png \
	report.txt \
	tensor.png \
	tf1.py \
	tf2.py \
	tf3.py \
	tf5.py \
	tf6.py \
	tf7.py


all: ${FN}.html 

${FN}.md: ${FN}.raw.md $(PY)
	m4 -P ${FN}.raw.md >${FN}.md

${FN}.html: ${FN}.md
	blackfriday-tool ./${FN}.md ${FN}.html
	echo cat ./${DIR}/md.css ${FN}.html >/tmp/${FN}.html
	cat ./${DIR}/css/pre ./${DIR}/css/markdown.css ./${DIR}/css/post ./${DIR}/md.css ./${DIR}/css/hpre ${FN}.html ./${DIR}/css/hpost >/tmp/${FN}.html
	mv /tmp/${FN}.html ./${FN}.html
	echo "file://${PP}/${FN}.html" >open.1

aa:
	echo "file://${PP}/${FN}.html" >open.1
