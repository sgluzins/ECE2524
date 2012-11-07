CC	= g++
CFLAGS	= -Wall
OBJS	= exptrtest.o driver.o parser.tab.o scanner.o

all: exprtest

exprtest: $(OBJS)
	$(CC) exprtrtest.o driver.o parser.tab.o scanner.o -o exprtest

exprtrtest.o: 
	$(CC) $(CFLAGS) -c exprtrtest.cpp

driver.o: driver.cpp scanner.hpp driver.hpp
	$(CC) $(CFLAGS) -c driver.cpp

parser.tab.o: parser.ypp
	$ bison parser.ypp

scanner.o: scanner.cpp scanner.hpp
	$ flex -t scanner.ll > scanner.cpp

clean: 
	rm -rf * .o exprtest
