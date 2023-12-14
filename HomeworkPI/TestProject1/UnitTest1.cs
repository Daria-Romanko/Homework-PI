using HomeworkPI;
using Microsoft.VisualStudio.TestPlatform.TestHost;
using System.Threading.Tasks;

namespace TestProject1
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void ZeroingTest1()
        {
            int n = 666;
            HomeworkPI.HomeworkPI.Zeroing(ref n);
            Assert.That(606, Is.EqualTo(n));
        }

        [Test]
        public void ZeroingTest2()
        {
            int n = 777;
            HomeworkPI.HomeworkPI.Zeroing(ref n);
            Assert.That(707, Is.EqualTo(n));
        }

        [Test]
        public void DoubleMinTest() 
        {
            Assert.That(12.625, Is.EqualTo(HomeworkPI.HomeworkPI.DoubleMin(12.625, 15)));
            
        }
    }
}