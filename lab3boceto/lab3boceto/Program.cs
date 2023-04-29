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

