#ifndef LERARQUIVO_H
#define LERARQUIVO_H

#include<iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <math.h>

using namespace std;

class LerArquivo{
    public:

    FILE* arquivoDeInstancia;
    size_t dimensao;
    int nVeiculos;
    int capacidadeDoVeiculo;
    string rota;
    vector<vector <int>> distanciaMatriz;
    vector<int> demanda;

    LerArquivo(){}
    LerArquivo(char* rotaDaInstancia);
    LerArquivo(char* rotaDaInstancia, bool flag);
    ~LerArquivo();

    void printData();
};

#endif