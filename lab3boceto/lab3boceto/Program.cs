using System;
using System.IO;
using System.Linq;
 static void Main(string[] args)
        {
            Console.Title = "Laboratorio no. 3 Daniela Morales";
            try
            {
                var maxBudget = GetMaxBudget(PathAuctions);
                Console.WriteLine("Este es el presupuesto más alto: " + maxBudget);

                var dpi = GetDpiWithMaxBudget(PathAuctions, maxBudget);
                Console.WriteLine("Este es el DPI con presupuesto más alto: " + dpi);

                var signature = GenerateSignature(PathCustomers, dpi);
                Console.WriteLine("Esta es la firma del usuario: " + signature);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Hubo un error: " + ex.Message);
            }
        }

private static int GetMaxBudget(string path)
        {
            var max = 0;
            foreach (var line in File.ReadLines(path))
            {
                var budgetIndex = line.IndexOf("\"budget\": ");
                if (budgetIndex == -1) continue;

                var budgetString = line.Substring(budgetIndex + 10).Split(',', '}')[0];
                var budget = int.Parse(budgetString);
                if (budget > max) max = budget;
            }
            return max;
        }

        private static string GetDpiWithMaxBudget(string path, int maxBudget)
        {
            foreach (var line in File.ReadLines(path))
            {
                var dpiIndex = line.IndexOf("\"dpi\": ");
                if (dpiIndex == -1) continue;

                var dpiString = line.Substring(dpiIndex + 8).Split(',', '}')[0];
                var dpi = int.Parse(dpiString);

                var budgetIndex = line.IndexOf("\"budget\": ");
                if (budgetIndex == -1) continue;

                var budgetString = line.Substring(budgetIndex + 10).Split(',', '}')[0];
                var budget = int.Parse(budgetString);

                if (budget == maxBudget) return dpiString;
            }
            throw new ArgumentException("No se encontró DPI para el mayor presupuesto.");
        }
