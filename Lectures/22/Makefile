
FN=Lect-22
DIR=../..
PP=`pwd`

PY= Dnn-Errors-2.png \
	Cullis-Patrick-Maroon-Bells-01.jpg \
	Dnn-Errors-2.png \
	maroon-bells_nightscape_rnclark_c09.28.2013.lf3-bin8x8shs.jpg \
	mistakes-of-the-past.png \
	Picture-At-Night.png \
	Screen-Shot-2020-11-10-at-13.07.41-PM.png

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
