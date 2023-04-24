using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace InmueblesGT
{
    class Program
    {
        static void Main(string[] args)
        {
            // Pedir al usuario que ingrese todas las líneas de entrada en un solo string
            Console.WriteLine("Ingrese todas las entradas separadas por un salto de línea:");
            string inputString = Console.ReadLine();

            // Dividir el string de entrada en líneas
            string[] inputLines = inputString.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);

            // Procesar cada línea de entrada
            foreach (string line in inputLines)
            {
                // Deserializar la línea del archivo Json
                dynamic data = JsonConvert.DeserializeObject(line);

                // Obtener los valores de input1 e input2
                List<Dictionary<string, bool>> map = data.input1.ToObject<List<Dictionary<string, bool>>>();
                List<string> requirements = data.input2.ToObject<List<string>>();

                // Procesar la información y obtener las recomendaciones de apartamentos
                List<int> recommendations = GetApartmentRecommendations(map, requirements);

                // Imprimir las recomendaciones en la consola
                Console.WriteLine(JsonConvert.SerializeObject(recommendations));
            }

          
        }
    }
}
