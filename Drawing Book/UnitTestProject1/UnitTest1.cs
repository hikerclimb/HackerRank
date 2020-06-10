using DrawingBook;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace UnitTestProject1
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            Program a = new Program();
            int expected = a.pageCount(6, 2);
            Assert.AreEqual(expected, 1);
        }

        [TestMethod]
        public void TestMethod2()
        {
            Program a = new Program();
            int expected = a.pageCount(6, 1);
            Assert.AreEqual(expected, 0);
        }

        [TestMethod]
        public void TestMethod3()
        {
            Program a = new Program();
            int expected = a.pageCount(5, 4);
            Assert.AreEqual(expected, 0);
        }

        [TestMethod]
        public void TestMethod4()
        {
            Program a = new Program();
            int expected = a.pageCount(6, 5);
            Assert.AreEqual(expected, 1);
        }

        [TestMethod]
        public void TestMethod5()
        {
            Program a = new Program();
            int expected = a.pageCount(6, 4);
            Assert.AreEqual(expected, 1);
        }

        [TestMethod]
        public void TestMethod6()
        {
            Program a = new Program();
            int expected = a.pageCount(4, 4);
            Assert.AreEqual(expected, 0);
        }

        [TestMethod]
        public void TestMethod7()
        {
            Program a = new Program();
            int expected = a.pageCount(7, 4);
            Assert.AreEqual(expected, 1);
        }
    }
}
