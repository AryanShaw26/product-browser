import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import CategoryFilter from "./components/CategoryFilter";
import ProductList from "./components/ProductList";
import Loader from "./components/Loader";
import { getProducts } from "../src/services/productApi";
import "./App.css";

function App() {
  const [products, setProducts] = useState([]);
  const [cursor, setCursor] = useState(null);
  const [snapshot, setSnapshot] = useState(null);
  const [category, setCategory] = useState("");
  const [loading, setLoading] = useState(false);

  const loadProducts = async (reset = false) => {
    setLoading(true);

    try {
      const data = await getProducts({
        cursor: reset ? null : cursor,
        snapshot: reset ? null : snapshot,
        category,
      });
      console.log(data);
      console.log(data.products);

      if (reset) {
        setProducts(data.products);
      } else {
        setProducts((prev) => [
          ...prev,
          ...data.products,
        ]);
      }

      setCursor(data.next_cursor);
      setSnapshot(data.snapshot);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  useEffect(() => {
    setCursor(null);
    setSnapshot(null);
    loadProducts(true);
  }, [category]);

  return (
    <>
      <Navbar />

      <div className="container">
        <CategoryFilter
          category={category}
          setCategory={setCategory}
        />

        <ProductList products={products} />

        {loading && <Loader />}

        {!loading && cursor && (
          <button
            className="load-btn"
            onClick={() => loadProducts()}
          >
            Load More
          </button>
        )}
      </div>
    </>
  );
}

export default App;