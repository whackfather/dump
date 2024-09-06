TARGET = ncmain.exe
SRC_FILES = ncmain.cpp

CXX = g++
CFLAGS = -Wall -g
OBJECTS = $(SRC_FILES:.cpp=.o)

$(TARGET): $(OBJECTS)
	$(CXX) -o $@ $^

%.o: %.cpp
	$(CXX) $(CFLAGS) -o $@ -c $<
