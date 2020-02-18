#include "../include/LerArquivo.h"

using namespace std;


LerArquivo::LerArquivo(char* rotaDaInstancia){

    this->rota = rotaDaInstancia;
    this->arquivoDeInstancia = fopen(rotaDaInstancia, "r"); //lendo arquivos de instancia 
    this->dimensao = 0;
    this->nVeiculos = 0;
    this->capacidadeDoVeiculo = 0;
    
    if(!this->arquivoDeInstancia){cout<<"Não foi possível abrir o arquivo!"<<endl;exit(-1);}
    
    char name[64];

    fscanf(this->arquivoDeInstancia, "NAME: %s\n", &name);
    fscanf(this->arquivoDeInstancia, "DIMENSION: %d\n", &this->dimensao);
    fscanf(this->arquivoDeInstancia, "VEHICLES: %d\n", &this->nVeiculos);
    fscanf(this->arquivoDeInstancia, "CAPACITY: %d\n", &this->capacidadeDoVeiculo);

    this->demanda = vector<int>(this->dimensao, 0);
    int lixo;
    fscanf(this->arquivoDeInstancia, "DEMAND_SECTION:\n");
    for(int i = 0; i < dimensao; i++){
        fscanf(this->arquivoDeInstancia,"%d %d", &lixo, &this->demanda[i]);
    }

    fscanf(this->arquivoDeInstancia, "\n");
    fscanf(this->arquivoDeInstancia, "EDGE_WEIGHT_SECTION\n");
    this->distanciaMatriz = vector< vector<int> >(dimensao, vector<int>(dimensao, 0));
    for(int i = 0; i < dimensao; i++){
        for(int j = 0; j < dimensao; j++){
            fscanf(this->arquivoDeInstancia,"%d", &this->distanciaMatriz[i][j]);
        }
    }
    // fclose(instanceFile);
}



