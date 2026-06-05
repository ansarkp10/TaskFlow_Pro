export default function ProjectCard({ project }) {

  return (
    <div className="border p-4 rounded shadow">

      <h2 className="text-xl font-bold">
        {project.name}
      </h2>

      <p className="mt-2">
        {project.description}
      </p>

    </div>
  );
}