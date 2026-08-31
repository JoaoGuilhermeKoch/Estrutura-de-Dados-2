#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

struct Aluno {
    char nome[50];
    int idade;
    float notas[3];
};

int main() {

    Aluno alunos[5];

    // CADASTRO DOS 5 ALUNOS
    for (int i = 0; i < 5; i++) {

        cout << "\n===== CADASTRO DO ALUNO " << i + 1 << " =====\n";

        cout << "Nome: ";
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cin.getline(alunos[i].nome, 50);

        cout << "Idade: ";
        cin >> alunos[i].idade;

        for (int j = 0; j < 3; j++) {
            cout << "Nota " << j + 1 << ": ";
            cin >> alunos[i].notas[j];
        }
    }

    // MOSTRA TODOS OS ALUNOS E SUAS MEDIAS
    cout << "\n";
    cout << "========================================\n";
    cout << "       MEDIAS DE TODOS OS ALUNOS       \n";
    cout << "========================================\n";

    float maiorMedia = 0;
    int posicaoMaior = 0;

    for (int i = 0; i < 5; i++) {

        float media = (alunos[i].notas[0] +
                       alunos[i].notas[1] +
                       alunos[i].notas[2]) / 3.0;

        cout << "\nAluno " << i + 1 << ": " << alunos[i].nome << endl;
        cout << "Media: " << fixed << setprecision(2) << media << endl;

        // Verifica a maior media
        if (i == 0 || media > maiorMedia) {
            maiorMedia = media;
            posicaoMaior = i;
        }
    }

    // MOSTRA O ALUNO COM A MAIOR MEDIA
    cout << "\n";
    cout << "========================================\n";
    cout << "            MAIOR MEDIA                 \n";
    cout << "========================================\n";

    cout << "Aluno: " << alunos[posicaoMaior].nome << endl;
    cout << "Media: " << fixed << setprecision(2) << maiorMedia << endl;

    cout << "\n";
    system("pause");

    return 0;
}