import axios from "axios";

const API = axios.create({
  baseURL: "https://product-browser-j5ow.onrender.com",
});

export const getProducts = async ({
  cursor = null,
  snapshot = null,
  category = null,
}) => {
  const params = {};

  if (cursor) params.cursor = cursor;
  if (snapshot) params.snapshot = snapshot;
  if (category) params.category = category;

  const res = await API.get("/products", { params });

  return res.data;
};