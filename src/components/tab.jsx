
function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export default function Tab({ categories }) {
  return (
    <div className="top-0 sticky overflow-clip bg-gray-100 border-b border-gray-200 ">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 sm:block">
        <nav className="-mb-px flex space-x-8 space-x-reverse">
          {categories.map((tab, index) => (
            <a
              key={tab.name}
              href={'#' + tab.id}
              className={classNames(
                index == 0
                  ? "border-primary text-primary font-bold"
                  : "border-transparent font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300",
                "whitespace-nowrap py-4 px-1 border-b-2 text-base"
              )}
              aria-current={tab.current ? "page" : undefined}
            >
              {tab.name}
            </a>
          ))}
        </nav>
      </div>
    </div>
  );
}
