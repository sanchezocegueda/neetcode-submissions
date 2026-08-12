class Singleton:

    _privateSingleton = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._privateSingleton is None:
            cls._privateSingleton = object.__new__(cls)
            
        
        return cls._privateSingleton

    def getValue(self) -> str:
        return getattr(self, "value", None)

    def setValue(self, value: str):
        self.value = value
