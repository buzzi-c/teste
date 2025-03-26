using System;
public override
using System.IO;

 

class Program

{

    static void Main()

    {

        string filePath = "C:\\Users\\Public\\dlp_test.txt";

       

        string sensitiveData = "Cartão de Crédito: 4111-1111-1111-1111\n" +

                               "CPF: 123.456.789-00\n" +

                               "Senha: SuperSecreta123";

       

        try

        {

            File.WriteAllText(filePath, sensitiveData);

            Console.WriteLine("Arquivo criado com sucesso em: " + filePath);

        }

        catch (Exception ex)

        {

            Console.WriteLine("Erro ao criar o arquivo: " + ex.Message);

        }

    }

}