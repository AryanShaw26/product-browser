function ProductCard({ product }) {
  return (
    <div className="card">
      <h3>{product.name}</h3>

      <p>
        <strong>Category:</strong> {product.category}
      </p>

      <p>
        <strong>Price:</strong> ₹{product.price}
      </p>

      <p>
        <strong>Updated:</strong>{" "}
        {new Date(product.updated_at).toLocaleString()}
      </p>
    </div>
  );
}

export default ProductCard;