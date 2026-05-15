interface Props {
    title: string;
    value: string | number;
}

export default function statCard({ title, value }: Props) {
    return (
        <div className="bg-gray-800 rounded-lg p-4">
            <h2 className="text-gray-400 text-sm">{title}</h2>
            <p className="text-white text-2xl font-bold">{value}</p>
        </div>
    );
}

