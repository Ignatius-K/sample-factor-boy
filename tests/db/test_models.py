class TestModels():

    def test_repr_str_brand_model(self, brand_factory):

        brand = brand_factory.build(
            name="Test Brand"
        )

        assert brand.__str__() == "Test Brand"

    
    def test_repr_str_vehicle_model(self, vehicle_factory):
        
        vehicle = vehicle_factory.build(
            name="Test Vehicle"
        )

        assert vehicle.__str__() == "Test Vehicle"