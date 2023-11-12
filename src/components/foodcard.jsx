import { PlusIcon } from "@heroicons/react/24/solid";

export default function FoodCard({ food }) {
  return (
    <li
      key={food.id}
      className="border-grey-200 border rounded-md flex overflow-hidden"
    >
      <div className="flex-shrink-0">
        <img
          className="w-24 h-24 md:w-44 md:h-44 rounded-r-md object-cover"
          src={food.image}
        />
      </div>

      <div className="p-5 flex-1 flex flex-col">
        <div className="flex-1">
          <h4 className="text-sm  md:text-base font-medium text-gray-700 hover:text-gray-800">
            {food.name}
          </h4>

          <p className="mt-1 text-xs text-gray-500">{food.description}</p>
        </div>
        <p className="text-left mt-4 text-lg font-bold text-gray-900">
          {food.price} {" ءتء"}
        </p>
        <button className="mt-2 bg-primary rounded-md py-2 px-6 justify-center flex items-center text-gray-700">
          <PlusIcon className="h-4 w-4 text-white ml-2" />
          <span className="text-xs font-medium text-white">
            اضافه کردن به سبد خرید
          </span>
        </button>
      </div>
    </li>
  );
}
