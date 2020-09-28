
FN=Lect-12
FN2=Podcast
DIR=../..
PP=`pwd`

all: ${FN}.html  ${FN2}.html

${FN}.html: ${FN}.md
	blackfriday-tool ./${FN}.md ${FN}.html
	echo cat ./${DIR}/md.css ${FN}.html >/tmp/${FN}.html
	cat ./${DIR}/css/pre ./${DIR}/css/markdown.css ./${DIR}/css/post ./${DIR}/md.css ./${DIR}/css/hpre ${FN}.html ./${DIR}/css/hpost >/tmp/${FN}.html
	mv /tmp/${FN}.html ./${FN}.html
	echo "file://${pp}/${FN}.html" >open.1

${FN2}.html: ${FN2}.md
	blackfriday-tool ./${FN2}.md ${FN2}.html
	echo cat ./${DIR}/md.css ${FN2}.html >/tmp/${FN2}.html
	cat ./${DIR}/css/pre ./${DIR}/css/markdown.css ./${DIR}/css/post ./${DIR}/md.css ./${DIR}/css/hpre ${FN2}.html ./${DIR}/css/hpost >/tmp/${FN2}.html
	mv /tmp/${FN2}.html ./${FN2}.html
	echo "file://${pp}/${FN2}.html" >open.1

aa:
	echo "file://${pp}/${FN2}.html" >open.1
