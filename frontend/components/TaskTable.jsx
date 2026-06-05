export default function TaskTable({ tasks }) {

  return (
    <table className="w-full border">

      <thead>

        <tr className="bg-gray-200">

          <th className="border p-2">
            Title
          </th>

          <th className="border p-2">
            Status
          </th>

          <th className="border p-2">
            Due Date
          </th>

        </tr>

      </thead>

      <tbody>

        {tasks.map((task) => (

          <tr key={task.id}>

            <td className="border p-2">
              {task.title}
            </td>

            <td className="border p-2">
              {task.status}
            </td>

            <td className="border p-2">
              {task.due_date}
            </td>

          </tr>

        ))}

      </tbody>

    </table>
  );
}