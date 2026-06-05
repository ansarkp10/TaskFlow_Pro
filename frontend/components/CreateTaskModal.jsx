"use client";

import { useState } from "react";

import API from "../services/api";

export default function CreateTaskModal() {

  const [formData, setFormData] = useState({
    title: "",
    description: "",
    status: "pending",
    project_id: "",
    assigned_to: "",
    due_date: "",
  });

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      await API.post("/tasks/", formData);

      alert("Task Created Successfully");

    } catch (error) {

      console.log(error);

      alert("Error Creating Task");

    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-4 border p-4 rounded"
    >

      <input
        type="text"
        placeholder="Title"
        className="border p-2"
        onChange={(e) =>
          setFormData({
            ...formData,
            title: e.target.value,
          })
        }
      />

      <textarea
        placeholder="Description"
        className="border p-2"
        onChange={(e) =>
          setFormData({
            ...formData,
            description: e.target.value,
          })
        }
      />

      <input
        type="number"
        placeholder="Project ID"
        className="border p-2"
        onChange={(e) =>
          setFormData({
            ...formData,
            project_id: Number(e.target.value),
          })
        }
      />

      <input
        type="number"
        placeholder="Assigned User ID"
        className="border p-2"
        onChange={(e) =>
          setFormData({
            ...formData,
            assigned_to: Number(e.target.value),
          })
        }
      />

      <input
        type="date"
        className="border p-2"
        onChange={(e) =>
          setFormData({
            ...formData,
            due_date: e.target.value,
          })
        }
      />

      <button
        type="submit"
        className="bg-black text-white p-2 rounded"
      >
        Create Task
      </button>

    </form>
  );
}